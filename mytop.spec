%include	/usr/lib/rpm/macros.perl
Summary:	tool for monitoring the threads and overall performance of MySQL
Name:		mytop
Version:	1.4
Release:	1
License:	GPL
Group:		Applications/Databases
Source0:	http://jeremy.zawodny.com/mysql/mytop/mytop-1.4.tar.gz
# Source0-md5:	c917f519bc3add1d09e1695351dbca70
URL:		http://jeremy.zawodny.com/mysql/mytop/
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mytop is a console-based (non-gui) tool for monitoring the threads and overall performance of MySQL 3.22.x, 3.23.x, and 4.x servers.

%prep
%setup -q

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/m*
%{_mandir}/man1/*
