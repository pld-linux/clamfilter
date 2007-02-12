Summary:	clamfilter - a small, efficient clamav content filter for Postfix
Summary(pl.UTF-8):   clamfilter - mały, lecz skuteczny filtr dla Postfiksa
Name:		clamfilter
Version:	0.5
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	http://www.ensita.net/products/clamfilter/%{name}-%{version}.tar.gz
# Source0-md5:	27047253d5eda132f93d276a31798e08
URL:		http://www.ensita.net/products/clamfilter/
Requires:	clamav
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a small, efficient clamav content filter for Postfix. What is
does is just a content filtering of messages passing via Postfix MTA
thru clamav.

%description -l pl.UTF-8
To jest mały, lecz efektywny filtr dla Postfiksa. Jego zadaniem jest
jedynie filtrowanie wiadomości, które przechodza poprzez MTA przez
clamava.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install clamfilter $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
